import pandas as pd
import re
import market_values_data as mv
import results_1x_x2.utility as ut

def process_file(year):
    file_path = f"italy/{year}-{(year+1)%2000}/1-seriea.txt"
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the content by lines
    lines = content.split('\n')

    # Regular expression patterns to extract match information
    matchday_pattern = re.compile(r'(Matchday \d+|\d+\^? Giornata)')
    date_pattern = re.compile(r'\[\w+\.? \d+\.\d+\.\]?')
    time_pattern = re.compile(r'\d{2}\.\d{2}')
    match_pattern_en = re.compile(r'(\d{2}\.\d{2})\s+([\w\s]+?)\s+(\d+)-(\d+)\s+\((\d+-\d+)\)\s+([\w\s]+)+|([\w\s]+?)\s+(\d+)-(\d+)\s+\((\d+-\d+)\)\s+([\w\s]+)')
    match_pattern_it = re.compile(r'([\w\s]+?)\s+(\d+)-(\d+)\s+([\w\s]+)')

    # Initialize an empty list to store match data
    matches = []

    # Track the current matchday and date
    current_matchday = None
    current_date = None

    # Determine the language and format of the file
    if "Matchday" in content:
        match_pattern = match_pattern_en
        is_english = True
    else:
        match_pattern = match_pattern_it
        is_english = False

    
    prev_match = {}
    
    # Process each line
    for line in lines:
        if matchday_pattern.search(line):
            current_matchday = matchday_pattern.search(line).group()
        elif date_pattern.search(line):
            current_date = date_pattern.search(line).group()
        elif match_pattern.search(line):
            if is_english:
                match_info = match_pattern.search(line).groups()
                if match_info[:6] != (None, None, None, None, None, None):
                    time, home_team, gol_home, gol_away, _, away_team = match_info[:6]
                else:
                    home_team, gol_home, gol_away, _, away_team = match_info[6:]
                    time = None
            else: # Italian
                match_info = match_pattern.search(line).groups()
                home_team, gol_home, gol_away, away_team = match_info
                time = None
            result = ut.get_result(int(gol_home), int(gol_away))
            # Values
            home_value = mv.get_market_value(year,home_team.strip())
            home_value_weight = float(home_value)/float(mv.get_max_market_value(year))
            away_value = mv.get_market_value(year,away_team.strip())
            away_value_weight = float(away_value)/float(mv.get_max_market_value(year))
            # Check and init Trend
            if not(home_team.strip() in prev_match):
                prev_match[home_team.strip()] = ut.generate_random_trend()
            if not(away_team.strip() in prev_match):
                prev_match[away_team.strip()] = ut.generate_random_trend()
            # Trend
            medium_points_home = sum(prev_match[home_team.strip()])/5
            medium_points_away = sum(prev_match[away_team.strip()])/5
            # Single past matches
            actual_prev_match_home = prev_match[home_team.strip()]
            actual_prev_match_away = prev_match[away_team.strip()]
            # Update the last 5 results
            prev_match[home_team.strip()] = prev_match[home_team.strip()][1:] + [ut.transform_result(result, True)]
            prev_match[away_team.strip()] = prev_match[away_team.strip()][1:] + [ut.transform_result(result, False)]
            matches.append([current_matchday, current_date, time, home_team.strip(), home_value, home_value_weight, gol_home,gol_away, away_team.strip(), away_value, away_value_weight, result, medium_points_home, medium_points_away, actual_prev_match_home[0], actual_prev_match_home[1], actual_prev_match_home[2], actual_prev_match_home[3], actual_prev_match_home[4], actual_prev_match_away[0], actual_prev_match_away[1], actual_prev_match_away[2], actual_prev_match_away[3], actual_prev_match_away[4]])

    # Create a DataFrame from the match data
    df = pd.DataFrame(matches, columns=['Matchday', 'Date', 'Time', 'Home Team', 'Home Value', 'Home Value Weight', 'Home Goals', 'Away Goals', 'Away Team', 'Away Value', 'Away Value Weight', 'Result', 'Medium Points Home', 'Medium Points Away',
                                        'Home Match 1', 'Home Match 2', 'Home Match 3', 'Home Match 4', 'Home Match 5', 'Away Match 1', 'Away Match 2', 'Away Match 3', 'Away Match 4', 'Away Match 5'])
    # Verify that each matchday has exactly 10 matches
    print(f'Processing {year}...')
    for matchday in df['Matchday'].unique():
        count = df[df['Matchday'] == matchday].shape[0]
        if count != 10:
            print(f'Warning: {matchday} has {count} matches instead of 10')
        else:
            print(f'{matchday} has 10 matches')

    # Save the DataFrame to a CSV file
    csv_file_path = f'C:/Users/utente/Desktop/Unibs/Progetti/AI/Football/file_csv/serie_a_{i}-{(i+1)%2000}.csv'
    df.to_csv(csv_file_path, index=False)

    csv_file_path


for i in range(2013, 2025):
    process_file(i)
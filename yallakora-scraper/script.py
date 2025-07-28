import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

def main():
    date = datetime.date.today().strftime('%m/%d/%Y')
    url = f'https://www.yallakora.com/match-center?date={date}'
    page = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    
    if page.status_code != 200:
        print(f"Failed to load page: {page.status_code}")
        return
    
    src = page.content
    soup = BeautifulSoup(src, 'lxml')
    score_board = soup.find_all('div', {'class': 'matchesList'})
    match_details = []
    
    def get_matches_info(board):
        
        title = board.find('h2').text.strip()
        all_matches = board.find_all('div', {'class': 'teamsData'})
        
        for i in range(len(all_matches)):
            try:
                teamA = all_matches[i].find('div', {'class': 'teamA'}).find('p').text.strip()
                teamB = all_matches[i].find('div', {'class': 'teamB'}).find('p').text.strip()
                
                time = all_matches[i].find('span', {'class': 'time'}).text.strip()
                
                all_scores = all_matches[i].find_all('span', {'class': 'score'})
                scoreB = all_scores[1].text.strip()
                scoreA = all_scores[0].text.strip()
                score = f'{teamB} {scoreB} - {scoreA} {teamA}'
                
                match_details.append({
                    "Champion": title,
                    "Team A": teamA,
                    "Team B": teamB,
                    "Score": score,
                    "time": time,
                    "date": date
                })
            except Exception:
                continue
            
    for i in range(len(score_board)):
        get_matches_info(score_board[i])
        
    pd.DataFrame(match_details).to_excel('data.xlsx')

main()
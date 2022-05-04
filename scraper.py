from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

trending_youtube_url = 'https://www.youtube.com/feed/trending?bp=4gIKGgh0cmFpbGVycw%3D%3D'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument("--disable-setuid-sandbox")
  driver = webdriver.Chrome(options = chrome_options)
  return driver

def get_videos(driver):
  video_div_class = 'ytd-video-renderer'
  #print("Fetching the page title...")
  #print(driver.title)
  driver.get(trending_youtube_url)
  videos = driver.find_elements(By.TAG_NAME, video_div_class)
  return videos
  
if __name__ == "__main__":
  print("Creating driver...")
  driver = get_driver()

  print("Fetching trending videos...")
  videos = get_videos(driver)

  print(f'Found {len(videos)} videos')

  
  
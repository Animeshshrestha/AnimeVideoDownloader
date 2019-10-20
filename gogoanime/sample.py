import requests, json

from clint.textui import progress

with open('episodes.json') as f:
  data = json.load(f)

name_of_anime = data[0].get('name')

def search_episode(episode):
	
	for d in data:
		if d["title"].lower() == name_of_anime.lower()+str(episode):
			return [d["download_link"],d["title"]]

def search_multi_episode(episode):

	multi_episode_name = [name_of_anime.lower()+str(x) for x in episode[:4]]

	item = []
	
	for d in data:
		for m in multi_episode_name:
			if d.get('title').lower() == m:
				item.append([d.get('download_link'), d.get('title')])

	return item
	# to do 
	# multi = []
	# try:
	# 	for d in data:
	# 		for c in multi_episode_name:
	# 			if d["title"].lower() == c:
	# 				multi.append(d["download_link"])
	# 				return multi
	# except:
	# 	pass




def download_only_single_episodes(download_link,episode_name):
	local_filename = episode_name+'.mp4'
	# NOTE the stream=True parameter
	r = requests.get(download_link, stream=True)
	with open(local_filename, 'wb') as f:
		print("Downloading File Name",local_filename)
		total_length = int(r.headers.get('content-length'))
		for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(int(total_length)/1024) + 1): 
			if chunk: # filter out keep-alive new chunks
				f.write(chunk)
	r.close()
	return local_filename

def prompt_user_to_enter():

	mode = input("Do you want to Download:\n A) Single Episodes.\n B) Multiple Episodes. \n [A/B]? :")

	if mode.lower() == "a":
		print("Write function to download single episodes only")
		episode = int(input("Please enter the  episode number to download"))

		ep = search_episode(episode)
		download_only_single_episodes(ep[0],ep[1])
		print("Finished")

	if mode.lower() == "b":

		episode = [int(x) for x in input("Enter multiple value: ").split()]
		mu_ep = search_multi_episode(episode)
		
		for i in mu_ep:
			download_only_single_episodes(i[0], i[1])
		print("Finished")


prompt_user_to_enter()







import os
import shutil
import xml.etree.ElementTree as ET


def parse_xml(root, id_list, text_list):
	children = root.getchildren()
	if len(children) == 0:
		return
	else:
		for child in children:
			# if child.tag != 'TextView':
			# 	parse_xml(child, id_list, text_list)
			# if child.tag != 'ImageView':
			# 	parse_xml(child, id_list, text_list)
			attribs = child.attrib
			for key in attribs.keys():
				if '}text' in key:
					if key.rindex('text') == len(key) - 4:
						if attribs[key] not in text_list:
							text_list.append(attribs[key])
				if '}src' in key:
					if key.rindex('src') == len(key) - 3:
						if attribs[key] not in id_list:
							id_list.append(attribs[key])
			parse_xml(child,id_list,text_list)

def get_relevant_activity(app, act_list):
	# enter call graphs dirs
	f = open('' + app, 'r')
	methods = []
	relevant_activities = []
	for line in f.readlines():
		line = line.strip('\n').split('\t')
		for l in line:
			if l not in methods:
				methods.append(l)
			else:
				continue
	f.close()
	for method in methods:
		for activity in act_list:
			if activity in method:
				if activity not in relevant_activities:
					relevant_activities.append(activity)
				else:
					continue
			else:
				continue
	return relevant_activities




def main(dir):
	apps = os.listdir(dir)
	for app in apps:
		if (app == '.DS_Store'):
			continue
		print(app)
		os.mkdir('./UI_Context/storage/' + app[:app.index('.txt')] + '/')
		#enter output file dirs
		f = open('' + app, 'r')
		app_activities_layouts = {}
		app_activities = []
		for line in f.readlines():
			line = line.strip('\n').split('\t')
			app_activities_layouts[line[0]] = line[1]
			app_activities.append(line[0])
		f.close()
		relevant_activity = get_relevant_activity(app, app_activities)
		relevant_activity_layout = []
		for activity in relevant_activity:
			layout = app_activities_layouts[activity]
			relevant_activity_layout.append(layout)
		if len(relevant_activity_layout) == 0:
			continue
		else:
			for activity in relevant_activity:
				layout = app_activities_layouts[activity]
				apk_context_text = []
				#apk resource dirs
				apk_res_dir = ''
				apk_name = app[:app.index('.txt')]
				activity_xml = apk_res_dir + apk_name + '.apk/res/layout/' + layout + '.xml'
				try:
					tree = ET.parse(activity_xml)
				except Exception as e:
					continue
				apkdata_text = []
				apkdata_id = []
				parse_xml(tree.getroot(), apkdata_id, apkdata_text)
				for text in apkdata_text:
					if '@string' in text:
						string_id = text[text.index('/') + 1:]
						f_string = open(apk_res_dir + apk_name + '.apk/res/values/strings.xml', 'r')
						for line in f_string.readlines():
							if string_id not in line:
								continue
							try:
								string_value = str(line)[str(line).index('>') + 1:str(line).index('</')]
								apk_context_text.append(string_value)
							except Exception as e:
								continue
					else:
						apk_context_text.append(text)
				f_out = open('./UI_Context/storage/' + app[:app.index('.txt')] + '/' + activity + '.txt', 'w')
				for text in apk_context_text:
					f_out.write(text + ' ')
				f_out.close()


if __name__ == 	"__main__":
	#app dirs
	app_dir = ''
	main(app_dir)
	# tree = ET.parse(xml_file)
	# apkdata_text = []
	# apkdata_id = []
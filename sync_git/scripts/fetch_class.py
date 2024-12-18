#!/usr/bin/env python3

import os, json, subprocess, pprint, csv

home_dir = os.path.expanduser("~")
script_dir = os.path.dirname(os.path.realpath(__file__))
CLASS_dir = os.path.join(home_dir, "CLASS")
JSON_path = os.path.join(script_dir, "../CLASS.json")
GIT_path = os.path.join(script_dir, "../GIT.csv")

os.makedirs(CLASS_dir, exist_ok=True)
print("Created CLASS/ directory in user directory")

with open(JSON_path, "r") as file:
    json_data = json.load(file)

git_repos = {}
main_branches = {}

for _subject in json_data: 
    for _class in json_data[_subject]:
        class_data = json_data[_subject][_class]
        git_name = f"ldnelson16/{_subject}{_class}.git"
        git_repos[f"{_subject}/{_class}"] = git_name
        main_branches[f"{_subject}/{_class}"] = "master"
        if "projects" in class_data:
            for project in class_data["projects"]:
                main_branch = "master"
                if len(project.split("?")) > 1:
                    main_branch = project.split("?")[1]
                    project = project.split("?")[0]
                project_name = project.split("~")[0]
                if len(project.split("~")) > 1:
                    git_name = project.split("~")[1]
                else:
                    git_name = f"ldnelson16/{_subject}{_class}-p{project}.git"
                git_repos[f"{_subject}/{_class}/projects/{project_name}"] = git_name
                main_branches[f"{_subject}/{_class}/projects/{project_name}"] = main_branch
        if "labs" in class_data:
            for lab in class_data["labs"]:
                main_branch = "master"
                if len(lab.split("?")) > 1:
                    main_branch = lab.split("?")[1]
                    lab = lab.split("?")[0]
                lab_name = lab.split("~")[0]
                if len(lab.split("~")) > 1:
                    git_name = lab.split("~")[1]
                else:
                    git_name = f"ldnelson16/{_subject}{_class}-l{lab}.git"
                git_repos[f"{_subject}/{_class}/labs/{lab_name}"] = git_name
                main_branches[f"{_subject}/{_class}/labs/{lab_name}"] = main_branch

# pprint.pprint(git_repos, indent=2)

with open(GIT_path, "w") as file:
    writer = csv.writer(file)
    
    # Write each key-value pair as a row
    for key, value in git_repos.items():
        writer.writerow([key, value, main_branches[key]])

    print("Stored repos to fetch in ~/dotfiles/sync_git/scripts/GIT.csv")
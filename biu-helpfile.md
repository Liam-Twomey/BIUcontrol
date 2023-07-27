Helpful commands for BIU usage

## Using the gh cli for login and cloning
`gh auth login`
	logs in to the github CLI interface. Choose <github.com>, then <https>,
	then copy the code and enter into the webrowser. DO NOT use ctrl+C to
	copy, as that will exit the process instead.

`gh repo clone <user>/<repo>
	Once logged in to gh, can be used to clone a repo for local work.

## Staging and committing changes
`git status`
	reports the status of changes to the file before committing relative to the latest commit.
`git add <directory>`
	stages changes to the file or directory given. Used to add new files.
`git commit -m "<commit message>"`
	commit the staged files, using <message> as the reqired commit message.
`git commit -am "<commit message>"`
	stages all changes to files in the directory and commits them. Use only for small changes.

## Interacting with the remote repo
`git push origin HEAD`
	pushes last commit on local branch to remote repo (github repo).
`git pull origin`
	`fetches` version of all files from github and `merges` with the local branch.
	fetch: gets history of the repo from the tracked repo
	merge: integrates changes from the remote repo into the local branch.

## Scenarios
### If adding a new file, newfile.txt to the gh repo...
	```bash
	cd <path to cloned gh repo>
	git add newfile.txt
	git commit -m "added newfile.txt"
	git push origin HEAD
	```
### If updating local directory from remote
	```bash
	git pull origin
	```

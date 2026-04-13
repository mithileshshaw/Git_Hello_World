# -------------------------------------------------------------------
# This is 2nd github learning session and exploring command
# link : https://www.youtube.com/watch?v=Kr8l7rQGwNs&t=14164s&pp=ygUVZ2l0IGh1YiBieSBhbnNoIGxhbWJh
# -------------------------------------------------------------------

    git status
    # git cofig --global user.email "mithilesh9shaw@gmail.com"
    # git --config --global user.name "mithilesh9shaw" or "mith_shaw" : existing one
    git init
39:00   .git is hidden folder we need to enable/disable it
        git status
42:15   git branch : Branch details
43:30   Initial commit is to register the master branch
        git add .
        git commit - m "initial commit"
        git branch : main
49:00   lets discuss every building blocks now
1:14:20 git commit : cand add message in actual file header or terminal header
1:21:10 New Branch will be created from head of the branch or latest commit
1:23:17 git log-
1:25:40 git log --oneline
1:35:20 .gitignore :- mention file name to avoid tracking some file under git initialised folder
1:35:50 git add .
        git status
1:38:40 Git dont track empty folder. It track folder with content only
        git status : run after creating empty folder and then after creating non empty folder
        bronze/ : adding in .gitignore to make untrack
1:42:00 .gitkeep : create .gitkeep file under silver folder to forcefully keeping track of non empty folder for future purpose
1:44:00 Brnaches details begins
        git branch
1:54:35 git switch main : always switch to main branch before creating any new branch 
        git checkout main : mainly used for multipurpose task like checking,switching branch etc. avoid using it for just switch

1:58:30 Working and Editing file on feature_mith_1 file begins from here
        git checkout -c feature_mith_1 or git switch -c feature_mith_1
		git branch
        git add .
        git commit -m "adding data on feature_mith_1"
        git log --online : 24095f1 (HEAD -> feature_mith_1) adding data on feature_mith_1
2:03:00 git switch main : head moves to main and the changes made in featue brnch disappers
       

2:05:30	Inviting another developer for contribution
		git switch main : first switch to main
2:07:10	git checkout -b feature_shaw_1 : feature_shaw_1 comes to same level of main
        git add .
        git commit -m "Added details 2:05:30 to 2:07:10"
       
2:09:15	git switch main
		git add .
		git commit -m "added details 2:09:15"

2:13:00 Merging
		git switch main
		git merge feature_shaw_1
		git status : nothing to commit but then also commit is mandatory
                git add .
                git commit -m "confict megred with feature_mith_1

2:15:00	2 types of merge Fast Forward Merge and Non-Fast Forword Merge
	Fast Forward Merge : created new branch, done two commit, but not make/commit prgress on main branch. Here Feature branch is ahead of main
		             Now we will merge both feature and main together later
	Non-Fast Forword Merge: In Real example we will move forward with main branch as well. Here Main branch is ahead of Feature
				Now we will merge both feature and main together and called Merge Commit

2:17:50	git merge feature_mith_1
        git add .
        git commit -m "confict megred with feature_mith_1

you can skip the from 2:20:40 to 2:35:50 alredy covered with feature_shaw_1 and feature_mith_1 merging
# 2:20:40 Merge Conflict
# 2:27:00	git switch main
# 		git switch -c bugfix : now start making some changes in file having bugfix branch codes
# 		git add .
# 		git commit -m "fix-bug"
# 		git switch main : again make changes in file having main brach codes
# 		git add . 
# 		git commit -m "bug is fixed"
# 		git status : nothing to commit
# 		git branch : main
# 		git merge bugfix -m "simple merge" : getting conflict
# 2:31:10	git merge --abort : to abort the merging
# 		git status
		
# 2:32:10	Now fixing the bugs/conflicts
# 		git merge bugfix -m "this guy fixed as well"
# 2:35:30	Click Complete Merge and then continue : after considering current OR incoming OR both current and incoming OR Manual Resolution OR Reset to base\
# 2:35:50	git status : conficts are resolved but now we need to commit to conclude the merges
# 		git add .
# 		git commit -m "conflicts merged".
                comment: Adding this extra line just for bugfix2 in main branch and commit it

2:38:10 Now we will work on same file but still dont get the conflict
        git switch -c bugfix2
        We are writing in fresh new line for bigfix2 so, there will be not much conflict and we will resolve it manually also
        git add .
        git commit -m "adding new content for bugfix2 and will not get conflict"
        git merge bugfix2 : The current changes and incoming chagnes dont have much conflict and manually editing it for final changes
        git status
        git add . 
        git commit -m "Manualy resolved bugfix2 from main branch, by using merge command"

2:46:45 Rebase : shifting the base of featrue branch to new commit of the maaster branch. 
        Its a kind of Fast Forward mode. Now if we apply Merge command after Rebasing it then it becomes Merge FF
        That means we do not have new commits in main branch, all the commits are coming from featues branch

2:51:14 git status : main
        git add .
        git commit -m "commiting to explore rebase"
        git switch -c rebase_feat

2:51:50 Rebase starts exploring
        git add .
        git commit -m "added data fore reabase branch"
2:52:30 git switch main : add some new data
        git add .
        git commit -m "add some new data"

2:53:00 Rebase command 
        git switch rebase_feat
        git rebase main
        git merge rebase_feat : Fast-Forward merge because the were no additional commit available in main branch

2:56:40 Lets talk about Ref log and Time Travelling
        Delte some file or file data
        git add .
        git commit -m "delete some data"
        git reflog : advance version of git --oneline
3:02:40	git reset --hard HEAD~1
3:04:00	git rest --hard 3accb4c : use commit id to go back again to present/acutal version

3:07:50	git diff
        git add .
        dit diff : nothing
        dif diff --staged : diff b/w staging area and destination
        git reset : moving back from staging area and making file again as modified
        Go to Source Control and discard changes as per wish

3:12:00	Cherry Pick
3:15:00	Merging only requried commit from feature branch out of multiple commit and will be assigned with new commit id
        git switch rebase_feat : add some new details
        git add .
        git commit -m "exploring cherry-pick"
        git add . : add some more details
        git commit -m "exploring cherry-pick 2"
        git switch main
        git log --oneline : select the desire commit id for cherry-pick
        git cherry-pick 47904f1
3:23:00	git cherry-pick 47904f1 82992ff : for multiple cherry-pick

3:24:00 Stashing : Temporary storage location that git provides
        git switch -c dev1
        add . : add some details or modify code
        git commit -m "commiting dev1 for stashing"
		adding some more details in progress and will keep this work in stashing before switching branch
        git switch main
3:30:00 Stashing explain
3:31:20 git stash push -m "My Dev paused"

3:32:10 git switch main : switched successfully after stashing
        git add .
        git commit -m "commiting after stashing"

3:33:00 git switch dev1
        git stash list : stash@{0}: On dev1: My Dev paused
3:36:25 git stash apply
        git stash list
        git stash pop : to delete from stack memory possible only before commit
        add .
        git commit -m "commit from retreiving stashing"

3:40:00 git stash push -m "add again for stashing"
        git stash list
        git switch main
        git switch dev1
        git stash apply "stash@{0}" : using stash id to get back content from stash stack
        git add .
        git commit -m "commiting by git stash apply stash id"

3:44:00 Create GIT_GAT Reporsitory
        git config --global user.name "mithilesh shaw"
        git config --global user.email "mithiles9shaw@gmail.com"
        git config --list   #check git configured details
		
3:46:00	Create GIT_GAT Reporsitory
		Setting --> Developer Setting --> Token(classic) --> Generate new token (classic) --> 
		https://github.com/mithileshshaw/GIT_GAT.git
3:47:10	git remote -v : we should have remote version before push
3:47:35	git remote add origin https://github.com/mithileshshaw/GIT_GAT.git : origin is destination where you want to push the code
	git remote -v : now origin got added
	git switch main
	git branch -m main : to rename the branch from master to main

3:49:50	git push origin main :
3:49:50	git push -u origin main : will not allow you to push because u need to authenticate

3:52:25	git remote add origin https://<USERNAME>:<PERSONAL_ACCESS_TOKEN>@github.com/<OWNER>/<REPOSITORY_NAME>.git
                                https://mithileshshaw:<PERSONAL_ACCESS_TOKEN>@github.com/mithileshshaw/GIT_GAT.git
                To add a remote origin using a personal access token, you can embed the token directly in the HTTPS URL,

3:55:43	git pull origin main --allow-unrelated-histories

4:00:00	git clone "https://github.com/mithileshshaw/GIT_GAT.git"
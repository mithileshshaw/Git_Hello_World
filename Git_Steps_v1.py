# -------------------------------------------------------------------
# This is first github learning session and exploring command..
# link : https://www.youtube.com/watch?v=Ez8F0nW6S-w
# -------------------------------------------------------------------

command:
git --version
git init -- to initialise the local folder as a git folder

git clone https://github.com/mithileshshaw/mith_github_practice.git
git status

git config --global user.name "mithilesh shaw"
git config --global user.email "mithiles9shaw@gmail.com"
git config --list   #check git configured details

4 types of status :-
1. untracked -- new file that git doesn't yet track
2. modified -- changed
3. staged -- add or staging into github # status becomed staged file is ready to committed
4. unmodified -- by using commit the status of code or file becomes unchanged


ADD and Commit :-

1.  git add <-filename-> or git add . -- to add multiple file
        # add -- adds new or changed files in your working directory to the Git staging area
        
2. git commit -m "some message"
        # commit - it is the record of change
 
PUSH :-
3. git push origin main -- push the changes form GIT system to GIT Repository. Here origin is self decrlared or nick name to the repo we are using

39:00       
# From Local Repo to Github
cd ..
mkdir LocalRepo
ls -a
INIT Command:
git init -- to initialise this folder as a git repository
ls -a
make a new file to write a program
git add .
git status
git commin -m "message or add initial files"

42:44	make a new repositories where you want to push your local content and ignore README.md as of now
git remote add origin https://github.com/mithileshshaw/mith_github_practice_localrepo.git
    -- git remote remove orging  --to remove if wrong repos is linked
git remote -v -- to verify remote
git branch -- to check the brach name where we are master/main are same
git branch -M main : for renaming the branch
git push origin main or git push -u origin main : -u used to set upstream or to set default push to origin main if we are continously pushing to origin main
git push -- now use only this because -u is set as shortcut

49:34	General Wrokflow
		Git repo --> Clone --> Changes --> Add --> Commit --> Push

52:00 Branch sample Commands
		git branch -- to check branch
		git branch -M main -- to rename branch
		git checkout <branch name> -- to navigate
		git checkout -b <branch name> -- to create new branch
		git branch -d <branch name> to delete branch

# Branch details
git branch
git checkout -b feature1 -- create new branch
git checkout main   -- switch to another branch
git branch
git checkout feature1

git checkout -b feature2
git checkout main
git branch -d feature2 -- for deleting the branch but it will throw error if we try deleting if we are in same branch
git checkout main	-- first we need to change the branch
git branch -d feature2
    git push origin --delete feature2 -- Delete the remote branch but keep in local
    git branch -D feature2 -- force delete the branch even if it is not merged with main
git branch


git checkout feature1 -- and make some changes in coding file
git add .
git commit -m "add new feature"
git status -- working tree clean
git checkout main -- the changes in the file vanish that we mande in branch feature1
git checkout feature1 -- the changes in the file reappears automatically
git push origin feature1 -- pushing our changes to feature1 branch

# Merging the branch
# Way 1
git branch -- currently feature1
git diff main -- check diff in barches feature1 vs main
git merge main -- will check this later

58:00
# Way 2
Create a Pull Reqwuest -- It lets you tell others about changes you have pushed to a branch in a repo in Github
						-- we will see it tries to merge feature 1 into main branch
						-- Github will show No conflict with Green button means changes are done in differet line and not same line as in main
                        -- complete these steps in Github URL
Merge pull request --> Confirm merge -- > Pull request successfully merged and closed

git checkout main -- now you dont see feature1 changes even after pull req. since pull and merge done only on Github and not in Gitsystem
                    -- you need to pull all the details from github to local now
git pull origin main -- to bring remote changes into local . Now the changes are reflected in local also

# Resolving Merging Conflict
we are currently in main branch now and make some changes in index.html file
<p>This is a new feature1 (button)</p>
git add .
git commit -m "Add button"

git chekcout feature1
git branch -- currently set to feature1
<p>This is a new feature1 (dropdown)</p>
git add .
git commit -m "Add dropdown"

git diff main -- now we see the differnces in main and feature1 branches
git merge main -- at present we are at feature1 branch, now in VS code index.html you will see some messages
                -- choose wisely or you can manually correct the file by removing unncessary comments
                -- lets add both deatails as of now button and dropdown
git add .
git commit -m "Add both features"
git diff main -- you will see one differences extra in main branch

git checkout main -- now the feature1 changes got vanish
git merge feature1 -- now merging main with feature1.
                    -- this time no mergre conflict because changes this time changes are in different line. previously it was in same line
git push -- to push the changes and finally resolving the conflicst

# Undoing changes
# Case 1: Staged Changes
git branch -- we are in main branch
            -- delete dropdown feature from index.html
git add .
git status
            -- but now we realised that we have done some wrong changes and want to revert back
git reset <-filename->
git reset -- for multiple file revert
git satus -- we will see messages as Changes not staged for commit

# Case 2: Committed Changes (for one commit)
		-- # git reset HEAD~1

git add .
git commit -m "Delete button"
git status -- we will see comment as : Your branch is ahead of 'origin/main' by 1 commit
git reset HEAD~1 -- get back to 1 or 2 node back just like linked list the snapshot are saved
git status -- again the file is in unstaged
git log -- check the logs Press 'q' to exit

# Case 3: Commited Changes (for many commits)
# git reset <-commit hash->
# git reset --hard <-commit hash->

git reset a9b02e225087c181dda18311646864d40b2819b8 -- you will get from git log. it make changes only in git system but not in file
git status -- we can see file still in modified stage
git log -- now latest commit we can see as 'Add button'
git reset --hard a9b02e225087c181dda18311646864d40b2819b8 -- to make changes in both git system and vscode file also
git status -- nothing to commit, working tree clean. We can verify the vscode file is reverted


# FORK 
    -- A fork is a new repository that shares code and visibility settings with the original "upstream" repository
    -- Fork is rough copy
Steps -- Click on Fork, put your custom repository, Uncheck 'Copy the master branch only', Create fork
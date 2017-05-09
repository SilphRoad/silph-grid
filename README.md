# Silph Grid

The goal of this project is to provide a scalable, robust, production grade
backend to generate S2 coordinates / polygons for overlay on maps.

## Install

This is a stateless web application. It does not require any persistent data
stores but can make use of a caching layer, typically Redis, to provide quicker
responses and cut down on computation time.

## Develop

Fork this repository, clone your new fork, add upstream as a remote, create a
new branch. Hack on code, create a commit, push to your fork and open a pull
request. For completion, see the following:

### Create your repository

Fork the repository, replace `marcoceppi` with your username.

```
git clone git@github.com:marcoceppi/silph-grid.git
cd silph-grid
git remote add upstream https://github.com/SilphRoad/silph-grid.git
git fetch upstream
```

### Create a branch

This is where you will do you work. Typically create a new branch for each kind
of feature/issue you want to work on.

```
git checkout master
git fetch upstream
git merge --ff-only upstream/master
git checkout -b your-branch-name
```

### Commit changes

Do work, commit changes, push.

```
git add .
git commit -m "Describe the work you did"
git push origin your-branch-name
```

Open a new pull request.

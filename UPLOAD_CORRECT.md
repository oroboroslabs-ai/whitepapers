# UPLOAD TO GITHUB - CORRECT NAME

## STEP 1: CREATE GITHUB REPOSITORY
1. Go to: https://github.com/new
2. Repository name: **whitepapers**
3. Description: "Technical specifications and architectural documentation for the Oroboros stack"
4. Make it PUBLIC
5. DO NOT initialize with README (we already have one)
6. Click "Create repository"

## STEP 2: PUSH TO GITHUB
```bash
cd "J:/oroboros-programs/whitepapers"
git remote add origin https://github.com/oroboroslabs-ai/whitepapers.git
git push -u origin master
```

## STEP 3: ENABLE GITHUB PAGES
1. After push, go to: https://github.com/oroboroslabs-ai/whitepapers/settings/pages
2. Under "Build and deployment", select "Deploy from a branch"
3. Source: "Deploy from a branch"
4. Branch: "master"
5. Folder: "/(root)"
6. Click "Save"

## STEP 4: VIEW STATIC SITE
Your whitepapers will be available at:
**https://oroboroslabs-ai.github.io/whitepapers/**

## REPOSITORY URL
**https://github.com/oroboroslabs-ai/whitepapers**

## STATIC SITE URL
**https://oroboroslabs-ai.github.io/whitepapers/**

## DO THIS NOW - CREATE THE REPOSITORY NAMED "whitepapers"
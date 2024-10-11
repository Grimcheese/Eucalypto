# Contributing/Development Rules

The workflow to follow for development is as follows:
1. Work on new features on dev/<feature name> branch
2. Merge complete features/updates into dev-stage branch to be ran on the dev staging server using pull request
3. Workflow complete in pre-release phase

Any feature worked on related to an issue should be linked to that issue and referenced in the pull request.

## Version rules
Eucalypto uses the semantic versioning system major.minor.patch. 
Each merge to the dev-stage branch is an increment to the patch version number with the major number remaining 0 until the project is considered usable and functional. Minor version numbers can be incremented at certain milestones as different features are brought together and completed. 
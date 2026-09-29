# Required main-branch protection

## Week 1 status

The required protection policy is documented. The connected GitHub integration could not verify or configure repository branch protection because the administration endpoint returned HTTP 403.

This satisfies the Week 1 fallback requirement to provide explicit branch-protection instructions when administrative configuration cannot be verified. Actual repository enforcement remains **PENDING GITHUB ADMIN VERIFICATION**.

## Required settings for `main`

Configure:

1. Require a pull request before merge.
2. Require at least one approving review.
3. Dismiss stale approvals when new commits are pushed.
4. Require the `quality` and `compose-smoke` status checks.
5. Require the branch to be up to date before merge.
6. Require conversation resolution.
7. Disable force pushes.
8. Disable branch deletion.
9. Include administrators unless a documented exception is required.

A repository administrator should verify these settings before or immediately after the Week 1 PR is merged.

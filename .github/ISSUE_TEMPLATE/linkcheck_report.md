---
title: 🚨 Weekly linkcheck failed
about: Use this template for checking broken links
name: Weekly linkcheck failed
labels: Maintanance, bug
---

On devportal, we check the links on a weekly basis to ensure the links in on our docs are working.

The last ``linkcheck`` run failed, so it may have found broken links on the devportal docs. 

For full logs, check the [last workflow run](https://github.com/aiven/devportal/actions/workflows/linkcheck.yaml) on {{ date | date('dddd, MMM Do YYYY, hh:mm A') }} (UTC) to see the broken links and fix it.

Partial logs output can be found here:

{{ env.OUTPUT }}


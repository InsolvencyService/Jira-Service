issue_updated_json = {
  "user": {
    "displayName": "Andy Price",
  },
  "issue": {
    "key": "ADS-166",
    "fields": {
      "issuetype": {
        "name": "Story",
      },
      "assignee": {
        "displayName": "Andy Price",
      },
      "updated": "2017-02-14T11:51:10.766+0000",
      "summary": "Notify Service Management of Release",
      },
  },
}

expected_output_dict = {
    "story_number": "ADS-166",
    "title": "Notify Service Management of Release",
    "released_by": "Andy Price",
    "assignee": "Andy Price",
}

expected_empty_output_dict = {
    "story_number": "",
    "title": "",
    "released_by": "",
    "assignee": "",
}
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
            "customfield_11300": "James Warren",
            "customfield_11301": "2017-02-20",
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
    "transitioned_by": "Andy Price",
    "assignee": "Andy Price",
    "sign_off_by": "James Warren",
    "estimated_release_date": "2017-02-20"
}

expected_empty_output_dict = {
    "story_number": "",
    "title": "",
    "transitioned_by": "",
    "assignee": "",
    "sign_off_by": "",
    "estimated_release_date": ""
}
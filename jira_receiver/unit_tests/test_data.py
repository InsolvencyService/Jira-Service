issue_updated_json = {
    "user": {
        "displayName": "Andy Price",
        "emailAddress": "sixdaysandy@gmail.com",
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
                "emailAddress": "sixdaysandy@gmail.com",
            },
            "updated": "2017-02-14T11:51:10.766+0000",
            "summary": "Notify Service Management of Release",
            "reporter": {
                "emailAddress": "sixdaysandy@gmail.com",
                "displayName": "Andy Price",
            },
        },
    },
}

expected_output_dict = {
    "story_number": "ADS-166",
    "title": "Notify Service Management of Release",
    "transitioned_by": "Andy Price",
    "transitioned_by_email": "sixdaysandy@gmail.com",
    "assignee": "Andy Price",
    "assignee_email": "sixdaysandy@gmail.com",
    "reporter": "Andy Price",
    "reporter_email": "sixdaysandy@gmail.com",
    "sign_off_by": "James Warren",
    "estimated_release_date": "2017-02-20"
}

expected_empty_output_dict = {
    "story_number": "",
    "title": "",
    "transitioned_by": "",
    "transitioned_by_email": "",
    "assignee": "",
    "assignee_email": "",
    "reporter": "",
    "reporter_email": "",
    "sign_off_by": "",
    "estimated_release_date": ""
}
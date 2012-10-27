Requested Demonstration
====

Good day!

This project is a fully uninspired small schema and JSON API to serve
arbitrary resume data.  The core object is that of a 'Person', who may have
multiple resumes for different topics.  Each resume contains sections and
enough ordering and style hints to allow a renderer to produce a consistent
ordering and layout from one resume to the next.

Implementing this, I used [Django](http://www.djangoproject.com) and
[Tastypie](http://django-tastypie.readthedocs.org/en/latest/), two libraries I
have been playing with for another project, to provide the ORM and API
interfaces. This left very little (none, actually) code for me to write
directly, which seems like kind of a pity.  I assume that other similarly high
level languages would have equivalently powerful turnkey libraries to offer
this capability.  Since there was no code, that left no opportunity for unit
tests, per se, though I suppose I could have implemented some based off of the
test data fixtures, just to make sure the schema was set up correctly.  At
this point in the life of a project I probably would not, on the expectation
that the schema itself would be changing reasonably soon based on better
requirements.

As a side note, I think the most interesting programming assignment I ever
received was when I applied to Square back in '98 or '99: they wanted a fast
calculation of square roots, without yielding to any of the obvious solutions.
It turns out there are a lot of neat techniques for approximating that
mathematical operation.  None of which I remember anymore :)

I have supplied a basic fixture with enough data to demonstrate the format of
the output, reproduced here:

> http://host/resume/api/v1/person/?format=json

    {
      "meta": {
        "limit": 20, 
        "next": null, 
        "offset": 0, 
        "previous": null, 
        "total_count": 1
      }, 
      "page": 1, 
      "records": 1, 
      "rows": [
        {
          "email": "pine@apple.com", 
          "fname": "Pineapple", 
          "id": "1", 
          "lname": "Man", 
          "phone": "888-777-6666", 
          "resource_uri": "/resume/api/v1/person/1/", 
          "resumes": [
            "/resume/api/v1/resume/1/", 
            "/resume/api/v1/resume/2/"
          ]
        }
      ], 
      "total": 1
    }

> http://host/resume/api/v1/resume/1/?format=json

    {
      "page": 1, 
      "records": 1, 
      "rows": [
        {
          "id": "1", 
          "name": "Fruit Resume", 
          "person": {
            "email": "pine@apple.com", 
            "fname": "Pineapple", 
            "id": "1", 
            "lname": "Man", 
            "phone": "888-777-6666", 
            "resource_uri": "/resume/api/v1/person/1/", 
            "resumes": [
              "/resume/api/v1/resume/1/", 
              "/resume/api/v1/resume/2/"
            ]
          }, 
          "resource_uri": "/resume/api/v1/resume/1/", 
          "sections": [
            {
              "entries": [
                {
                  "byline": "Major Ingredient", 
                  "description": "Was a major component in the smoothie.", 
                  "end_date": "2012-05-05", 
                  "format_type": 1, 
                  "id": "1", 
                  "resource_uri": "/resume/api/v1/entry/1/", 
                  "start_date": "2012-01-01", 
                  "title": "Juice Club"
                }
              ], 
              "id": "1", 
              "mode": 1, 
              "resource_uri": "/resume/api/v1/entrysection/1/", 
              "title": "Blender Experience"
            }, 
            {
              "entries": [], 
              "id": "2", 
              "mode": 1, 
              "resource_uri": "/resume/api/v1/entrysection/2/", 
              "title": "Decorative Experience"
            }
          ]
        }
      ], 
      "total": 1
    }



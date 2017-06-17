# Api of 160znaków

# Data structures

## Post (object)
+ link (string) - link of web resource being described
+ description (string, 160 chars)
+ author (Author)
 
## Author (object)
+ name from github

# URLs
# Post [/post]
## List last entries [/]
+ Response 200 (application/json)
 + Attributes (array Post)

## New post [POST]
+ link
+ description

# Author [/author]
## Register [/register]
Using Github Oauth
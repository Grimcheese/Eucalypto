# Eucalypto

Eucalypto is a web hosted database that stores and displays information
about our plants. It stores information about indoor and outdoor plants,
plants in pots and plants in the ground. 

It will be able to record basic information about the plant, where it 
came from, when it was planted, where it is. There will also be images 
that can be linked to each plant.

Eucalypto will exist in two main ways: The website and the database.

This document provides a brief description of the project and in future
how to use the project. More specific information will be provided in 
the docs which can be viewed on the wiki page.

# Status

Main [![Build Status](https://drone.grimnet.work/api/badges/achawula/Eucalypto/status.svg?ref=refs/heads/main)](https://drone.grimnet.work/achawula/Eucalypto)

Staging [![Build Status](https://drone.grimnet.work/api/badges/achawula/Eucalypto/status.svg?ref=refs/heads/staging)](https://drone.grimnet.work/achawula/Eucalypto)

Latest dev push [![Build Status](https://drone.grimnet.work/api/badges/achawula/Eucalypto/status.svg?ref=refs/heads/dev)](https://drone.grimnet.work/achawula/Eucalypto)

## The website

The website will allow users to search and view plants that are stored 
in the database and allow users with authorisation to add new records
and update existing records in the database.

#### Pages
This functionality will require the following web pages
- Index page
- Plant page
- Login/Account page
- Upload form
- Update form

## The database

The database will contain tables storing data about plants and references
to images of the plants stored somewhere (probably the NAS). The actual
database implementation is still to be decided but general information 
to record can include:
- Common Name/s
- Family
- Genus
- Species
- Indoor/Outdoor
- Date planted
- Images
- Extra information

## Info




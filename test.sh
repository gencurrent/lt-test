#!/bin/sh

curl -H 'Accept:application/json; indent=4' -u suadmin:xTR3m3 'http://127.0.0.1:8000/api/organization/branch?name=Madrid'
curl -H 'Accept:application/json; indent=4' -u suadmin:xTR3m3 'http://127.0.0.1:8000/api/organization/branch?lat=1&lon=45'
curl -H 'Accept:application/json; indent=4' -u suadmin:xTR3m3 'http://127.0.0.1:8000/api/organization/employee?branch__name=London'
curl -H 'Accept:application/json; indent=4' -u suadmin:xTR3m3 'http://127.0.0.1:8000/api/organization/employee?branch__name=London&ordering=-id'

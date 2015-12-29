## Details
Language: go
Version: go1.5.2

Framework: None
Version: None

Packages used: database/sql, net/http, github.com/lib/pq

## Instructions:

In the server.go script:
	- Provide the Credentials for the Database
	- The CRUD queries can be changed
	- Start the server via `go run server.go` command
	- The server runs at: `http://127.0.0.1:9090`

## API's
	- GET API to perform psql CRUD operations at `http://127.0.0.1:9090/crud`
	- GET API to sleep for `a` milli seconds at `http://127.0.0.1:9090'/time_block?ms=a`

PSQL_PARAMS= {
	"host" : "host_ip",
	"user" : "test1",
	"password": "mypassword",
	"port": "5432",
	"dbname": "testdb"
}

CRUD_KEYS = ["create","read","update","delete"]

QUERY_DICT = {
	"create" : "INSERT INTO data_source(primary_id, data_int, data_string) VALUES(100,100,'Go Go Go');",
	"read": "SELECT * from data_source;",
	"update": "UPDATE data_source set data_string='GoGoGo' where data_int=100;",
	"delete": "DELETE from data_source where data_int=100;"
}
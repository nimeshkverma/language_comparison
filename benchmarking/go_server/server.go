package main

import (
    "fmt"
    "database/sql"
    "net/http"
    _ "github.com/lib/pq"
    "time"
    "strconv"
)

const (
    DB_USER     = "nimesh"
    DB_PASSWORD = ""
    DB_NAME     = "benchmarking_db"
)

func perform_crud(w http.ResponseWriter, r *http.Request) {

    dbinfo := fmt.Sprintf("user=%s password=%s dbname=%s sslmode=disable",
        DB_USER, DB_PASSWORD, DB_NAME)
    db, err := sql.Open("postgres", dbinfo)
    checkErr(err)
    defer db.Close()

    // INSERT Query
    fmt.Fprintf(w, "INSERT QUERY \n")
    _ , err = db.Query(`INSERT INTO data_source(primary_id, data_int, data_string) VALUES(100,100,'Go Go Go');`)
    checkErr(err)

    // SELECT Query
    fmt.Fprintf(w, "SELECT QUERY \n")
    _ , err = db.Query(`SELECT * from data_source;`)
    checkErr(err)

    //UPDATE Query
    fmt.Fprintf(w, "UPDATE QUERY \n")
    _ , err = db.Query(`UPDATE data_source set data_string=$1 where data_int=$2;`,"GoGoGo", 100)
    checkErr(err)

    //DELETE Query
    fmt.Fprintf(w, "DELETE QUERY \n")
    _ , err = db.Query(`DELETE from data_source where data_int=$1;`,100)
    checkErr(err)
    fmt.Fprintf(w, "TASK COMPLETED \n")
}

func checkErr(err error) {
    if err != nil {
        panic(err)
    }
}

func ms_block(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Server","A Go WebServer")
    w.Header().Set("Content-Type", "text/html")
    msecs, _ := strconv.Atoi(r.FormValue("ms"))
    time.Sleep(time.Duration(msecs) * time.Millisecond)
    fmt.Fprintf(w, "Slept for the given time duration!\n")

}

func main() {
    http.HandleFunc("/crud", perform_crud)
    http.HandleFunc("/time_block", ms_block)
    err := http.ListenAndServe(":9090", nil) // set listen port
    if err != nil {
        fmt.Println("ListenAndServe: ", err)
    }
}
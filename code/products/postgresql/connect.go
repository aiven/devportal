package main

import (
    "database/sql"
    "fmt"
    _ "github.com/lib/pq"
    "log"
)

func main() {
    serviceURI := "POSTGRESQL_URI"

    db, err := sql.Open("postgres", serviceURI)

    if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

    rows, err := db.Query("SELECT version()")
	if err != nil {
		panic(err)
	}

    for rows.Next() {
		var result string
		err = rows.Scan(&result)
		if err != nil {
			panic(err)
		}
		fmt.Printf("Version: %s\n", result)
	}
}

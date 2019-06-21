package main

import (
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"log"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hi there, I love %s!", r.URL.Path[1:])
}

func main() {
	// Setting Up database
	db, err := sql.Open("mysql", "root:@tcp(127.0.0.1:3306)/golangDB")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	// Checking the connections
	err = db.Ping()
	if err != nil {
		log.Fatal(err)
	}

	// Creating a model
	var (
		id   int
		name string
	)

	// Querying the database
	rows, err := db.Query("SELECT id, name FROM users;")
	if err != nil {
		log.Fatal(err)
	}
	defer rows.Close()

	// Parsing fetched data from database
	for rows.Next() {
		err := rows.Scan(&id, &name)
		if err != nil {
			log.Fatal(err)
		}
		log.Println(id, name)
	}
	err = rows.Err()
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("Server Running...")
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe(":3000", nil))
}

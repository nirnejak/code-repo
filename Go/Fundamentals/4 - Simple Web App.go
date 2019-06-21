package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/", index_handler)
	http.HandleFunc("/about/", about_handler)
	http.ListenAndServe(":8000", nil)
}

func index_handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Woah, Go is neat!")
}

func about_handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Expert web Design by Jittu")
}

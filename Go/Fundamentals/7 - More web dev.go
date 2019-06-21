package main

import (
	"fmt"
	"net/http"
)

func index_handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, `
			<h1>Hey there</h1>
			<p>Hey there</p>
			<p>...and simple!</p>
			<p>You %s even add %s </p>	
		`, "can", "<strong>variables</strong>")
	fmt.Fprintf(w, "<h1>Hey there</h1>")
	fmt.Fprintf(w, "<p>Hey there</p>")
	fmt.Fprintf(w, "<p>...and simple!</p>")
	fmt.Fprintf(w, "<p>You %s even add %s </p>", "can", "<strong>variables</strong>")
}

func main() {
	http.HandleFunc("/", index_handler)
	http.ListenAndServe(":8000", nil)
}

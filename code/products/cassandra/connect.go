package main

import (
	"flag"
	"fmt"
	"log"
	"time"

	"github.com/gocql/gocql"
)

func main() {
	var args = parseArgs()
	cassandraExample(args)
}

type Args struct {
	Host        string
	Port        int
	Username    string
	Password    string
	SSLCertfile string
}

func parseArgs() Args {
	var args Args
	flag.StringVar(&args.Host, "host", "", "Cassandra host")
	flag.IntVar(&args.Port, "port", -1, "Cassandra port")
	flag.StringVar(&args.Username, "user", "avnadmin", "Cassandra username")
	flag.StringVar(&args.Password, "password", "", "Cassandra password")
	flag.StringVar(&args.SSLCertfile, "ssl-certfile", "./ca.pem", "Path to project CA certificate")
	flag.Parse()

	if args.Host == "" {
		fail("-host is required")
	} else if args.Port == -1 {
		fail("-port is required")
	} else if args.Password == "" {
		fail("-password is required")
	}
	return args
}

func fail(message string) {
	flag.Usage()
	log.Fatal(message)
}

func cassandraExample(args Args) {
	var session = createSession(args)
	defer session.Close()
	createSchema(session)
	writeData(session)
	readData(session)
}

func createSession(args Args) gocql.Session {
	cluster := gocql.NewCluster(args.Host)
	cluster.ConnectTimeout = 10 * time.Second
	cluster.Port = args.Port
	cluster.ProtoVersion = 4
	cluster.Authenticator = gocql.PasswordAuthenticator{
		Username: args.Username,
		Password: args.Password,
	}
	cluster.SslOpts = &gocql.SslOptions{
		CaPath: args.SSLCertfile,
	}
	cluster.Consistency = gocql.Quorum

	session, err := cluster.CreateSession()
	if err != nil {
		log.Fatal(err)
	}
	return *session
}

func createSchema(session gocql.Session) {
	if err := session.Query(
		"CREATE KEYSPACE IF NOT EXISTS example_keyspace WITH REPLICATION = {'class': 'NetworkTopologyStrategy', 'aiven': 3}",
	).Exec(); err != nil {
		log.Fatal(err)
	}
	if err := session.Query(
		"CREATE TABLE IF NOT EXISTS example_keyspace.example_go (id int PRIMARY KEY, message text)",
	).Exec(); err != nil {
		log.Fatal(err)
	}
}

func writeData(session gocql.Session) {
	if err := session.Query(
		"INSERT INTO example_keyspace.example_go (id, message) VALUES (?, ?)", 1, "hello world",
	).Exec(); err != nil {
		log.Fatal(err)
	}
}

func readData(session gocql.Session) {
	iter := session.Query("SELECT id, message FROM example_keyspace.example_go").Iter()
	var id int
	var message string
	for iter.Scan(&id, &message) {
		fmt.Printf("Row: id = %d, message = %s\n", id, message)
	}
	if err := iter.Close(); err != nil {
		log.Fatal(err)
	}
}

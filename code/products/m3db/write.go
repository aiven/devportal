package main

import (
	"context"
	"fmt"
	"log"
	"time"

	"github.com/m3db/prometheus_remote_client_golang/promremote"
)

func main() {
	cfg := promremote.NewConfig(
		promremote.WriteURLOption(PROM_WRITE_URL),
		promremote.HTTPClientTimeoutOption(60*time.Second),
		promremote.UserAgent("aiven-docs/0.1"),
	)
	client, err := promremote.NewClient(cfg)
	if err != nil {
		log.Fatal(fmt.Errorf("unable to construct client: %v", err))
	}
	timeSeriesList := []promremote.TimeSeries{
		{
			Labels: []promremote.Label{
				{
					Name:  "__name__",
					Value: "cpu_temp_instant",
				},
			},
			Datapoint: promremote.Datapoint{
				Timestamp: time.Now(),
				Value:     83.0,
			},
		},
	}

	var ctx = context.Background()
	var writeOpts promremote.WriteOptions
	result, err := client.WriteTimeSeries(ctx, timeSeriesList, writeOpts)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Status code: %d\n", result.StatusCode)
}

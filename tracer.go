package main

import (
	"encoding/json"
	"fmt"
	"net"
	"net/http"
	"os"
	"time"
)

// GeoIP structure mapping standard network perimeter telemetry profiles
type GeoIP struct {
	IP          string `json:"ip"`
	CountryName string `json:"country_name"`
	Region      string `json:"region"`
	City        string `json:"city"`
	ASN         string `json:"asn"`
}

func executeNetworkTrace(target string) {
	fmt.Printf("[*] [Go Engine] Resolving DNS infrastructure for: %s\n", target)
	
	// Create an optimized local dialer context instance
	dialer := &net.Resolver{
		PreferGo: true,
		StrictErrors: false,
	}
	
	ips, err := dialer.LookupIPAddr(os.Background(), target)
	if err != nil {
		fmt.Printf("[!] Go Engine Error: Unable to resolve destination host mapping boundary: %v\n", err)
		return
	}

	httpClient := &http.Client{Timeout: 8 * time.Second}

	for _, ip := range ips {
		ipStr := ip.IP.String()
		fmt.Printf("[+] Resolved Public Host Interface: %s\n", ipStr)
		
		// Querying public reference API for geo-location routing metrics
		apiURL := fmt.Sprintf("https://ipapi.co/%s/json/", ipStr)
		resp, err := httpClient.Get(apiURL)
		if err != nil {
			fmt.Printf("    [!] Geolocation lookup skip: Routing query timeout.\n")
			continue
		}
		
		var record GeoIP
		err = json.NewDecoder(resp.Body).Decode(&record)
		resp.Body.Close()
		
		if err == nil && record.CountryName != "" {
			fmt.Printf("    Location Metrics: %s, %s, %s\n", record.City, record.Region, record.CountryName)
			fmt.Printf("    Autonomous System: %s\n", record.ASN)
		}
	}
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("[!] Go Engine Usage: ./tracer <domain_or_ip>")
		os.Exit(1)
	}
	executeNetworkTrace(os.Args[1])
}

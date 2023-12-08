Piped-data Parser

Starting SQL Server:
    
    docker compose up sql -d

Running

    docker compose up --build run

Calling

    curl -XPOST localhost:8080/2015-03-31/functions/function/invocations -d @event-sample.json

# ETL Data Engineer Workflow
 This Python application automates one of data engineer tasks. It extracts data from Excel spreadsheets that holds mobile-app reporting data for the first half-year 2020. 
 Performs transformations and calculations to generate new business metrics, stores the processed data in a MySQL database, and creates data visualizations to facilitate business insights. This can be valuable for various departments within an organization to analyze their data and make data-driven decisions.

## Additional Considerations:
- The application's functionality can be modified to aligns with the complexity of your ETL job requirements.
- While this application currently doesn't handle personal sensitive information, it's important to prioritize security considering ** PII's Encryption ** for any sensitive data you might use in the future.
- The application is designed to handle growing data volumes. Additionally, the calculated metrics can be seamlessly  ** integrated ** and migrated to any public cloud provider.

## Business goals:
- The main goal here is to bring in new customers and increase a company’s customer base.
- Create loyalty programs that will make customers stay longer and even refer family and friends. 

## Project Structure
```
ETL-challenge/
├── docker-compose.yml
└── python/
    ├── Dockerfile
    ├── main.py
    ├── appMarketing.xlsx
    └── requirements.txt
└── mysql/
    ├── Dockerfile
    └── marketing_db.sql
```

#### The processing application basically fetches the data and calculate two metrics:
 
- The network that usually has the most active users on a daily basis.
- The network that has the best “Installs” to “Subscription started” conversion rate.


### Useful docker commands:
- Rebuild and Run Your Docker-compose Setup
` docker-compose up --build `

- List all images
` docker images `

- Remove specific image
` docker rmi <image_id> `

- Force delete all images:
` docker rmi -f $(docker images -aq) `

- List all containers
` docker container ls `

- Remove specific container
` docker rm <container_id> `

- Stop and Clean existing Docker resources:

    ` docker-compose down `

    ` docker volume prune -f `

    ` docker network prune -f `

    ` docker image prune -f `

- Restart Docker Service:
    ` sudo systemctl restart docker `


### Verifying the two Metrics inside mysql-container
The two metrics should now be stored in the MySQL database marketing_db withtin mysql container. To verify use these commands to connect and query the tabels:

` docker-compose up -d  `

` docker ps `

```  docker exec -it <container_id> mysql -uroot -prootpassword ``` 

```sql
use marketing_db;
show tables;
select date, network, max(max_dau) as max_dau from most_active_networks group by date, network;
select date, max(conversion_rate) as best_rate from best_conversion_network group by date;
```

![charts](metrics.png)
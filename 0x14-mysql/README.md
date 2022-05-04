![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/280/KkrkDHT.png)

# 0x14. MySQL

------------

## General

- What is the main role of a database
- What is a database replica
- What is the purpose of a database replica
- Why database backups need to be stored in different physical locations
- What operation should you regularly perform to make sure that your database backup strategy actually works

## Conceps

- https://intranet.hbtn.io/concepts/49
- https://intranet.hbtn.io/concepts/68

------------

## List of poinst.

|  Point | What is done at this point? | level |
| ------------ | ------------ | ------------ | 
| 0x14-mysql | First things first, let’s get MySQL installed on both your web-01 and web-02 servers. | Mandatory | 
| 0x14-mysql | In order for us to verify that your servers are properly configured, we need you to create a user and password for both MySQL databases which will allow the checker access to them. | Mandatory |
| 0x14-mysql | In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from. | Mandatory |
| 0x14-mysql | Before you get started with your primary-replica synchronization, you need one more thing in place. On your primary MySQL server (web-01), create a new user for the replica server. | Mandatory |
| 4-mysql_configuration_primary, 4-mysql_configuration_replica | Having a replica member on for your MySQL database has 2 advantages: | Mandatory |
| 5-mysql_backup | What if the data center where both your primary and replica database servers are hosted are down because of a power outage or even worse: flooding, fire? Then all your data would inaccessible or lost. That’s why you want to backup and store them in a different system in another physical location. This can be achieved by dumping your MySQL data, compressing them and storing them in a different data center. | Mandatory |

------------

# Resources

- https://computingforgeeks.com/how-to-install-mysql-on-ubuntu-focal/
- https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication
- https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql
- https://www.databasejournal.com/ms-sql/developing-a-sql-server-backup-strategy/

------------

# Author

## Juan Sebastian Avendaño Gonzalez:
- Git: https://github.com/AvendanoisPepe
- Twitter: https://twitter.com/Sebastian_Aven
- Linkedin: https://www.linkedin.com/in/juan-sebastian-avenda%C3%B1o-gonz%C3%A1lez-8b1185200/

------------


![](https://i.imgur.com/HPJ8Qn8.jpg)
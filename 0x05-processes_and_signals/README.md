![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/Vxotqyj.png)

# 0x05. Processes and signals

------------

## General

- What is a PID
- What is a process
- How to find a process’ PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored

------------

## List of poinst.

|  Point | What is done at this point? | level |
| ------------ | ------------ | ------------ |
| 0-what-is-my-pid | Write a Bash script that displays its own PID. | Mandatory |
| 1-list_your_processes | Write a Bash script that displays a list of currently running processes. | Mandatory |
| 2-show_your_bash_pid | Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process. | Mandatory |
| 3-show_your_bash_pid_made_easy | Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash. | Mandatory |
| 4-to_infinity_and_beyond | Write a Bash script that displays To infinity and beyond indefinitely. | Mandatory |
| 5-dont_stop_me_now | We stopped our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this. | Mandatory |
| 6-stop_me_if_you_can | Write a Bash script that stops 4-to_infinity_and_beyond process. | Mandatory |
| 7-highlander | Write a Bash script that displays: | Mandatory |
| 8-beheaded_process | Write a Bash script that kills the process 7-highlander. | Mandatory |

------------

## List of repository files:

|  Point | own comments.  | level |
| ------------ | ------------ | ------------ |
| 0-what-is-my-pid | Con echo imprimo el PID | Mandatory |
| 1-list_your_processes | ps (process status) | Mandatory |
| 2-show_your_bash_pid | gep: puedes buscar una palabra o patrón y se imprimirá la línea o líneas que la contengan. | Mandatory |
| 3-show_your_bash_pid_made_easy | Busca en la lista de procesos para localizar el PID a partir del nombre (similar a ps | grep), La opción -l le dice a pgrep que muestre el nombre del proceso junto con su ID: | Mandatory |
| 4-to_infinity_and_beyond |Usar el comando de suspensión para agregar un retraso durante un período de tiempo específico. | Mandatory |
| 5-dont_stop_me_now | Matamos el proceso del anterior ejercicio | Mandatory |
| 6-stop_me_if_you_can | lo mismo que kill pero con p | Mandatory |
| 7-highlander | se supone que con SIGTERM manda el mensaje | Mandatory |
| 8-beheaded_process | se elimina el proceso del ejericio anterior. | Mandatory |

------------

# Documentation:
### Links:

- https://www.thegeekstuff.com/2012/03/linux-signals-fundamentals/
- https://www.thegeekstuff.com/2012/03/linux-processes-environment/
- http://www.linfo.org/pid.html
- https://www.hostinger.co/tutoriales/comando-grep-linux
- https://linuxize.com/post/pgrep-command-in-linux/
------------

# Author


## Juan Sebastian Avendaño Gonzalez:
- Git: https://github.com/AvendanoisPepe
- Twitter: https://twitter.com/Sebastian_Aven
- Linkedin: https://www.linkedin.com/in/juan-sebastian-avenda%C3%B1o-gonz%C3%A1lez-8b1185200/

------------


![](https://scontent.fbog4-1.fna.fbcdn.net/v/t39.30808-6/271153206_3074657909465585_6907762404450913633_n.jpg?_nc_cat=105&ccb=1-5&_nc_sid=730e14&_nc_ohc=DPFxC1wg0LkAX-PULpS&_nc_ht=scontent.fbog4-1.fna&oh=00_AT-7aF49a3-ThAgSU2ch0MBVSImH5gXD_YGNPLtK4rIg7Q&oe=62129E80)
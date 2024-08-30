# sudo docker run -d -t --name usename# conteinar-name
#sudo docker ps #@ -a
#sudo docker exec -it myubontu bash
# fast @ sudo pacman -U ./docker-desktop-<arch>.pkg.tar.zst
sudo pacman -S gnome-terminal
systemctl --user start docker-desktop
systemctl --user enable docker-desktop
sudo systemctl enable --now docker.service
sudo systemctl start --now docker.service
docker run -d -p 80:80 docker/getting-started


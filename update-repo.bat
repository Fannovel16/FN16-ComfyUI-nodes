::A shitty script to auto update the repo on my local machine lul
::Need someone to optimize it
cd comfy_controlnet_preprocessors
git checkout main
git add .
git commit -a -m %1
git push
cd ..\comfy_ckpt_utils
git checkout main
git add .
git commit -a -m %2
git push
cd ..
git submodule update --remote --merge
git add .
if [%3] == [] (git commit -m "Update custom nodes repo to the lastest version") else (git commit -m %3)
git push
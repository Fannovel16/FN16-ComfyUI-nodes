::A shitty script to auto update the repo on my local machine lul
::Need someone to optimize it
cd comfy_controlnet_preprocessors
git add .
git commit -m "%1"
git push
cd ..
git submodule update --remote --merge
git add .
git commit -m "Update custom nodes repo to the lastest version"
git push
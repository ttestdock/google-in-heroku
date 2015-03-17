##google in heroku

---
有时候访问google不便，需要这么一个逗比的东西

可以直接部署到heroku中

```bash
git clone ...
cd google-in-heroku
heroku create
git add -A
git commit -m "init"
git push heroku master
heroku open
```
搞定

compile:
	pip install -r requirements.txt

clean:
	find .  -name *.pyc -delete

run:
	python -m mlf projects.wx.metar

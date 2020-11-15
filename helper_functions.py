tz_str = None
sep = ' -- '
testFunctions = True

import datetime as dt

class dep_resolve:
    def pip_install():
      !pip install -U kaggle 
      !pip install -U transformers==2.9.1 
      !pip install -U pytorch-lightning==0.7.6
      !pip install -U aitextgen
    def atg_imports():
      import logging
      logging.basicConfig(
              format="%(asctime)s — %(levelname)s — %(name)s — %(message)s",
              datefmt="%m/%d/%Y %H:%M:%S",
              level=logging.INFO
          )
      from aitextgen import aitextgen
      from aitextgen.colab import mount_gdrive, copy_file_from_gdrive
      from aitextgen.TokenDataset import TokenDataset, merge_datasets
      from aitextgen.utils import build_gpt2_config
      from aitextgen.tokenizers import train_tokenizer
    def dep_resolve(skip_pip):
      if skip_pip == True:
        print('note: skip_pip is set to True, skipping pip.')
      elif skip_pip == False:
        print('note: skip_pip is set to False, installing dependencies with pip.')
        pip_install()
      else:
        print('note: skip_pip is not set to True or False, skipping pip.')

class kaggle:
  def kaggle_dl():
    !mkdir -p /root/.kaggle
    !mv kaggle.json /root/.kaggle/kaggle.json
    !chmod 600 /root/.kaggle/kaggle.json
    !rm -rf anime-subtitles.zip
    !kaggle datasets download -d jef1056/anime-subtitles
    !rm -rf 'Anime Datasets V3.zip'
    !rm -rf 'input (Cleaned).txt'
    !unzip anime-subtitles.zip
    !wc -l 'input (Cleaned).txt'

class time:
  def now(tz_str):
    tz_now = dt.datetime.now(tz_str)
    return tz_now
  def timestamp():
    rightnow = time.now(tz_str)
    stamp = str(rightnow)# + ' // TZ: ' + str(tz_str)
    return stamp

class logging:
  sep = ':'
  def println(msg, lvl):
    ln_timestamp = '@' + str(time.timestamp())
    lvl = '[' + lvl + ']'
    ln_str = ln_timestamp + sep + lvl + sep + msg + '\n'
    print(ln_str)

class housekeeping:
  def cleandir(rm_model, rm_tokenizer_data):
    if rm_tokenizer_data == True:
      !rm -rf aitextgen-merges.txt
      !rm -rf aitextgen-vocab.json
      logging.println('rm_tokenizer_data set to true, deleting tokenizer data at $PWD/aitextgen-merges.txt and $PWD/aitextgen-vocab.json', 'INFO')
    elif rm_tokenizer_data == False:
      logging.println('rm_tokenizer_data set to false, skipping tokenizer data deletion.', 'WARN')
    if rm_model == True:
      logging.println('rm_model is set to true, deleting model stored at trained_model.', 'INFO')
      !rm -rf /content/trained_model
    elif rm_model == False:
      logging.println('rm_model set to False, skipping model deletion.', 'WARN')
    else:
      logging.println('rm_model not set to True or False, skipping model deletion.', 'WARN')

class load:
  def load_csv(pth):
    x = pd.read_csv(pth)
    return x
  def load_json(pth):
    x = pd.read_json(pth)
    return x
  def load_xlsx(pth):
    x = pd.read_excel(pth)
    return x
  def load(pth, load_type):
    if load_type == 'csv':
      x = load_csv(pth)
      return x
    elif load_type == 'json':
      x = load_json(pth)
      return x
    elif load_type == 'xlsx':
      x = load_excel(pth)
      return x
    elif load_type == 'excel':
      x = load_excel(pth)
      return x
    else:
      logging.println('Incorrect load_type or load_type not found. Returning empty DataFrame', 'ERRR')
      x = pd.DataFrame()
      return x

class meta:
  def test_helpers():
    logging.println('Logging and timestamping seems to be working fine, testing functions...', 'TEST')
    logging.println('Testing housekeeping.cleandir(False)...', 'TEST')
    housekeeping.cleandir(False, False)

def test_decision(run_tests):
  if run_tests == True:
    logging.println('run_tests set to true, running tests.', 'INFO')
    meta.test_helpers()
  elif run_tests == False:
    logging.println('run_tests set to false, not running any tests on any functions besides logging.', 'WARN')
  else:
    logging.println('run_tests not set to true or false, not running any tests on any functions besides logging.', 'WARN')

test_decision(testFunctions)

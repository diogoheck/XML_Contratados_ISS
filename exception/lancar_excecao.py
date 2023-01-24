import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException


def lancamento_excecao(funcao, driver, *args, **kwargs):
    for i in range(kwargs.get('segundos', 10)):
        try:
            funcao(driver, *args)
            break

        except ElementNotInteractableException as e:
            print(f'Retry in {i} second', e, funcao.__name__)
            time.sleep(i)

        except NoSuchElementException as e:
            print(f'Retry in {i} second', e, funcao.__name__)
            time.sleep(i)

        except Exception as e:
            print(f'Retry in {i} second', e, funcao.__name__)
            time.sleep(i)


import logging
import ask_sdk_core.utils as ask_utils
import requests

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class chamadaInicial(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        fala_da_alexa = "O que deseja que sua plantinha faça?"

        return (
            handler_input.response_builder
                .speak(fala_da_alexa)
                .ask(fala_da_alexa)
                .response
        )

class CasoNaoAcheComando(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        logger.error(exception, exc_info=True)

        fala_da_alexa = "Desculpe, a plantinha esta confusa e não entendeu o seu comando"

        return (
            handler_input.response_builder
                .speak(fala_da_alexa)
                .ask(fala_da_alexa)
                .response
        )

class chamadaMolhar(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("chamadaMolhar")(handler_input)

    def handle(self, handler_input):
        fala_da_alexa = "OK, vou me molhar!"
        requests.get('https://url_api/molhar')

        return (
            handler_input.response_builder
                .speak(fala_da_alexa)
                .response
        )

class chamadaAcenderLuz(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("chamadaAcenderLuz")(handler_input)
        

    def handle(self, handler_input):
        fala_da_alexa = "Estava precisando de luz, obrigada!"
        requests.get('https://url_api/acender')

        return (
            handler_input.response_builder
                .speak(fala_da_alexa)
                .response
        )

class chamadaApagarLuz(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("chamadaApagarLuz")(handler_input)

    def handle(self, handler_input):
        fala_da_alexa = "Ok, vou para de fazer fotosintese e relaxar"
        requests.get('https://url_api/apagar')

        return (
            handler_input.response_builder
                .speak(fala_da_alexa)
                .response
        )

sb = SkillBuilder()

sb.add_request_handler(chamadaInicial())
sb.add_request_handler(chamadaAcenderLuz())
sb.add_request_handler(chamadaMolhar())
sb.add_request_handler(chamadaApagarLuz())
sb.add_exception_handler(CasoNaoAcheComando())

lambda_handler = sb.lambda_handler()

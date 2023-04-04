# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils
import json

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

from ask_sdk_core.utils import get_supported_interfaces
from ask_sdk_model.interfaces.alexa.presentation.apl import (
    RenderDocumentDirective,
    ExecuteCommandsDirective,
    SpeakItemCommand,
    AutoPageCommand,
    HighlightMode,
)

from bs4 import BeautifulSoup
import requests


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def _load_apl_document(file_path):
    ## type: (str) -> Dict[str, Any]
    """Load the apl json document at the path into a dict object."""
    with open(file_path) as f:
        return json.load(f)


url = 'https://swacademy.com/ar/courses/category/development-programs-1#'
response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, 'lxml')

tt = soup.find_all('div', class_= 'course-title')
names_program = []
for tag in tt:
    names_program.append(tag.a.text)
names_program[0] = names_program[0].split("- ٢٧/٠٢/٢٠٢٣")[0]


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "هلا"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "رعاك الله"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class lamha_swccIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("lamha_swcc")(handler_input)

    def handle(self, handler_input):
      
        speak_output = 'اِنْطِلَاقًا مِنْ إِدْرَاكِهَا لِأَهَمِّيَّةِ اَلتَّدْرِيبِ وَتَطْوِيرِ مَوَارِدِهَا اَلْبَشَرِيَّةِ قَامَتْ اَلْمُؤَسَّسَةُ اَلْعَامَّةُ لِتَحْلِيَةِ اَلْمِيَاهِ اَلْمَالِحَةِ فِي اَلْعَامِ 1402 هجري الموافق 1982 ميلادي بِتَأْسِيسِ وَإِنْشَاءِ مَرْكَزِ تَدْرِيبِ لِمَنْسُوبِي اَلْمُؤَسَّسَةِ فِي كُلٍّ مِنْ اَلْجُبَيْلْ وَجُدَّةَ ، وَمُنْذُ ذَلِكَ اَلْحِينِ بَدَأَتْ مَسِيرَةَ اَلتَّدْرِيبِ بِالْمُؤَسَّسَةِ وَتَطْوِيرِ مَوَارِدِهَا بِمُوَاكَبَةٍ أَحْدَثَ اَلْأَسَالِيبَ وَالنُّظُمَ وَالْمَنْهَجِيَّاتِ اَلتَّدْرِيبِيَّةَ فِي مَجَالِ صِنَاعَةِ اَلتَّحْلِيَةِ ، وَاسْتَمَرَّ اَلْعَطَاءُ وَالنُّمُوّ فِي هَذَا اَلْجَانِبِ عُقُودًا مِنْ اَلزَّمَنِ بَلَغَتْ 40 عَامًا - مِنْ فَضْلِ اَللَّهِ بِمُخْرِجَاتِ نَوْعِيَّةٍ يَشْهَدُ لَهَا سُوقُ اَلْعَمَلِ بِالْمُؤَسَّسَةِ وَخَارِجِهَا فِي اَلْقِطَاعَيْنِ اَلْعَامِّ وَالْخَاصِّ وَفِي اَلْعَامِ 2010 - 2011 بَدَأَ اَلْمَرْكَزُ تَقْدِيمَ اَلْخِدْمَاتِ اَلتَّدْرِيبِيَّةِ لِمَنْسُوبِي اَلْقِطَاعَاتِ اَلْأُخْرَى مِنْ خَارِجِ اَلْمُؤَسَّسَةِ بَعْد مُوَافَقَةِ مَجْلِسِ إِدَارَةِ اَلْمُؤَسَّسَةِ عَلَى اَلتَّشْغِيلِ اَلِاسْتِثْمَارِيِّ لِلْمَرْكَزِ وَذَلِكَ فِي إِطَارِ مَشْرُوعِ اَلتَّحَوُّلِ اَلتِّجَارِيِّ لِعَمَلِ اَلْمَرْكَزِ ، حَيْثُ اِسْتَقْطَبَ اَلْعَدِيدَ مِنْ اَلْعُمَلَاءِ فِي اَلْقِطَاعَيْنِ اَلْحُكُومِيِّ وَالْخَاصِّ ، مِنْ دَاخِلِ اَلْمَمْلَكَةِ وَخَارِجِهَا وَفِي اَلْعَامِ 2019 تَمَّ تَغْيِيرُ اَلْمُسَمَّى مِنْ مَرْكَزِ اَلتَّدْرِيبِ إِلَى  اَلْأَكَادِيمِيَّةِ اَلسُّعُودِيَّةِ لِلْمِيَاهِ  ، وَتَطْوِيرَ اَلْهُوِيَّةِ اَلْبَصَرِيَّةِ لَهَا لِتَفْتَحَ بِذَلِكَ آفَاقًا أَوْسَعَ مِنْ اَلتَّدْرِيبِ وَالِارْتِقَاءِ بِالْخِدْمَاتِ اَلتَّدْرِيبِيَّةِ وَالِانْتِشَارِ عَالَمِيًّا وَنَشْرِ اَلْمَعْرِفَةِ وَفْقَ رُؤْيَةٍ طَمُوحَةٍ تَهْدِفُ لِتَعْزِيزِ اِسْتِدَامَةِ إِنْتَاجِ اَلْمِيَاهِ ، وَتَطْمَحَ اَلْأَكَادِيمِيَّةُ إِلَى تَقْدِيمِ تَجْرِبَةٍ تَعْلِيمِيَّةٍ وَتَدْرِيبِيَّةٍ مُتَكَامِلَةٍ ، وَفْقً مَنْهَجِيَّاتٍ وَتِقْنِيَّاتِ اَلتَّعَلُّمِ اَلْحَدِيثَةِ ، وَالْمُتَوَافِقَةَ مَعَ اَلْمُسْتَهْدَفَاتِ اَلْحَالِيَّةِ وَالْمُتَطَلَّبَاتِ وَالِاحْتِيَاجَاتِ اَلتَّدْرِيبِيَّةِ لِسُوقِ اَلْعَمَلِ بِهَدَفِ اَلِارْتِقَاءِ وَالْعِنَايَةِ بِالْمَوْرِدِ اَلْبَشَرِيِّ وَتَهْيِئَتِهِ لِسُوقِ اَلْعَمَلِ كَأَحَدِ أَهَمَّ مُسْتَهْدَفَاتٍ رُؤْيَةِ اَلْمَمْلَكَةِ 2030'
        
        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )

class dor_swccIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("dor_swcc")(handler_input)

    def handle(self, handler_input):
      
        speak_output = "بحسـب التوقعات والإحصاءات فإن معدلات النمو في الجوانب السـكانية والاقتصادية والصناعية، ستشـهد طفرة كبيرة خلال السـنوات المقبلة، وهو ما يعتبر تحديًا بسـبب شـح الموارد الطبيعية المائية في المنطقة ولذلك فإن صناعة تحلية المياه المالحة سـتضطلع بدور محوري خلال الفترة القادمة، وستشـكل أهم الركائـز الداعمـة فـي توفيـر المـوارد المائيـة، مما يتطلب بالطبع تأهيل وتطويـر القوى العاملة لتعزيز كفاءتها وصقل مهاراتهـا لتولي قيادة قطاعات إنتاج المياه بالإضافة للنقل والتوزيع وكل ما يختص بصناعة المياه، ومن شـأنه أن يحقق مبدأ الاسـتدامة في الموارد الطبيعية"
        
        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class mnhag_swccIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("mnhag_swcc")(handler_input)

    def handle(self, handler_input):
      
        
        speak_output = "نعمـل فـي الأكاديميـة علـى توفيـر مسـارات تدريبية وبرامـج تعليمية تناسـب كافة الفئات والشـرائح وتتـراوح مـدة المسـارات و البرامـج التدريبيـة من 3 أيام و حتى 12 شـهًرا ،ونعتمدعلىأحـدثالتقنيات وأفضـل المنهجيـات المعتمـدة عالميًـا لتقديـم الخدمـات التدريبية بأعلى جـودة ممكنة، حيث نقدم التدريـب النظـري والعملـي فـي مجـال صناعـة التحليـة فـي بيئـة تدريبيـة متكاملـة تضـم عـددا مـن الممـاثلات أجهـزة المحـاكاة والورش والمعامل، وبواسـطة أكفأ المدربيـن والخبراء في هذا المجال"
        
        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )

class rowya_swccIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("rowya_swcc")(handler_input)

    def handle(self, handler_input):
      
        speak_output = "أَنْ نُصْبِحَ اَلْمَصْدَرَ اَلْعَالَمِيَّ اَلرَّئِيسَ لِمُحْتَرِفِي صِنَاعَةِ اَلْمِيَاهِ"
        
        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class rsalat_swccIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("rsalat_swcc")(handler_input)

    def handle(self, handler_input):
        speak_output = "نَجْلِبُ اَلْأَمْنُ اَلْمَائِيُّ إِلَى اَلْعَالَمِ عَبْرَ تَطْوِيرِ إِخْصَائِيِّ اَلْمِيَاهِ اَلْمُحْتَرِفِينَ وَتَمْكِينِهِمْ مِنْ تَصْمِيمٍ وَتَنْفِيذِ وَتَشْغِيلِ حُلُولِ نَوْعِيَّةٍ لِإِمْدَادَاتِ اَلْمِيَاهِ تَمْتَازُ بِالِاسْتِدَامَةِ وَالتَّكْلِفَةِ اَلْمُجْدِيَةِ"      

        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )

class targets_swccIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("targets_swcc")(handler_input)

    def handle(self, handler_input):
        list_ = [
            "تَأْهِيلُ كَوَادِرَ سُعُودِيَّةٍ مُمَيَّزَةٍ بِإِمْكَانِهَا أَنْ تَتَوَلَّى اَلرِّيَادَةُ فِي مَجَالِ صِنَاعَةِ تَحْلِيَةِ اَلْمِيَاهِ",
            "تَقْدِيمَ حُلُولٍ جَدِيدَةٍ وَمُبْتَكَرَةٍ لِإِمْدَادَاتِ اَلْمِيَاهِ",
            "قِيَادَةَ اَلْمُحْتَوَى اَلْمَعْرِفِيِّ فِي مَجَالِ اَلتَّنَاضُحِ اَلْعَكْسِيِّ وَتِقْنِيَّاتُ اَلتَّحْلِيَةِ اَلْحَدِيثَةِ",
            "رَفْعَ مَتُوىْ مَعَايِيرَ اَلْأَكَادِيمِيَّةِ مِنْ خِلَالِ اَلشَّرِكَاتِ وَالِاعْتِمَادَاتِ اَلدَّوْلِيَّةِ",
            "تَأْسِيسَ شَرَاكَاتِ اِسْتِرَاتِيجِيَّةٍ بَيْنَ اَلْأَكَادِيمِيَّةِ وَالْمُؤَسَّسَاتِ اَلْمُخْتَصَّةِ بِمَا يُعَزِّزُ اَلتَّعَاوُنُ وَتَبَادُلُ اَلْخِبْرَاتِ فِي مَجَالِ اَلتَّدْرِيبِ",
            "تَهْيِئَة بِيئَةٍ مُحَفِّزَةٍ وَاحْتِرَافِيَّةٍ لِلتَّدْرِيبِ",
            "تَعْزِيزَ مَفَاهِيمِ اَلْأَمْنِ اَلْمَائِيِّ عَلَى اَلْمُسْتَوَى اَلْمَحَلِّيِّ وَالْإِقْلِيمِيِّ وَالدَّوْلِيِّ",
            "دَعْمَ قِيَادَاتِ قِطَاعِ اَلْمِيَاهِ مَحَلِّيًّا وَدَوْلِيًّا",
            "إِطْلَاقَ بَرْنَامَجِ أَجْيَالِ اَلْمِيَاهِ لِلْأَطْفَالِ ",
            "إِطْلَاقَ اَلْبَرْنَامَجِ اَلْأَخْضَرِ لِلِاسْتِدَامَةِ اَلْبِيئَةِ",
            "إِنْشَاءَ مَتْحَفِ اَلْأَكَادِيمِيِّ اَلسُّعُودِيَّةِ اَلْمِيَاهَ"
            ]
        
        speak_output = ", ".join(list_)
        
        
        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )

class values_swccIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("values_swcc")(handler_input)

    def handle(self, handler_input):
        list_ = [
            "النزاهة و الشفافي",
            "اَلِابْتِكَار وَالتَّطْوِيرِ وَالِاسْتِدَامَةِ",
            "بــيـــئــة سليمة وآمـنــة",
            "الاحترافية والالــتـزام والــجـدية و النزاهة"
            ]
        
        speak_output = ", ".join(list_)
        
        
        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )

class stations_swccIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("stations_swcc")(handler_input)

    def handle(self, handler_input):
        list_ = [
            "سنة 1982 تم تأسيس مركز التدريب في الجبيل وجدة",
            "سنة 1987 تم الانتقال إلى مبنى مركز التدريب بالجبيل",
            "سنة 2008 تم افتتاح المعامل والورش بالمبنى الثاني"
            "سنة 2010 تم التحول التجاري لتغطية القطاعين العام والخاص تدريبياً",
            "سنة 2019 تم أعتماد الأسم الجديد للأكاديمية السعودية للمياه",
            "سنة 2020 تم أفتتاح مبنى السلامة والإطفاء"    
            ]
        
        speak_output = ", ".join(list_)
        
        
        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class marafaq_swccIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("marafaq_swcc")(handler_input)

    def handle(self, handler_input):
        list_ = [
             "٦٠ مدربًًا متخصص وذي خبرة",
             "٣٢ قاعة محاضرات واجتماعات وندوات",
             "٢٠ معمل وورشة تدريبية",
             "٧ مماثلات تدريبية",
             "مسرح يتسع لـ 700 شخص",
             "سكن متدربين مجهز بجميع المرافق يتسع لـ 240 متدرب",
             "مطعم يتسع لـ 120 شخص",
            ]
        
        speak_output = ", ".join(list_)
        
        
        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class masarat_swccIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("masarat_swcc")(handler_input)

    def handle(self, handler_input):
        list_ = [
           "مسار تأهيلي للمشغلين والفنيين 6 اشهر الي سنة لحديثي التخرج من المشغلين والفنيين من خريجي الكليات الصناعية والتقنية وما يعادلها",
           "مسار تأهيلي للمهندسين من 4 الي 6 أشهر لحديثي التخرج من المهندسين ويستهدف الخريجين في جميع التخصصات الهندسية",
           "مسار البرامج التطويرية من 3 ايام الي 3 اسابيع ويستهدف العاملين من ذوي الخبرة لرفع كفاءتهم وصقل مهاراتهم"
            ]
        
        speak_output = ", ".join(list_)
        
        
        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )

class masoula_swccIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("masoula_swcc")(handler_input)

    def handle(self, handler_input):

        
        speak_output = "نعمـل علـى تعزيـز اسـتدامة الأمـن المائـي، ومواجهة تحديـات نقص المـوارد المائية للمسـاهمة في حمايـة الأجيـال حاضـرا ومسـتقبلا مـن أي مخاطر تهـدد حياتهم ووجودهم"
        
        
        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )

class outputs_swccIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("outputs_swcc")(handler_input)

    def handle(self, handler_input):
        list_ = [
              "البرامج التطويرية اكثر من 63050 متدرب و 5680 برنامج تدريبي",
              "البرامج التأهيلية للمهندسين اكثر من 1593 متدرب و 41 برنامج تدريبي",
              "البرامج التأهيلية للفنيين اكثر من 5917 متدرب و 48 برنامج تدريبي"
            ]
        
        speak_output = ", ".join(list_)
        
        
        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )

class partener_swccIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("partener_swcc")(handler_input)

    def handle(self, handler_input):
        list_ = [
               "الفنار",
               "Saudi Aramco",
               "شَرِكَة اَلْمِيَاهِ اَلْوَطَنِيَّةِ",
               "وزارة الدفاع",
               "بترو رابغ",
               "المؤسسه العامه للري",
               "مرافق",
               "الشركة السعودية لصناعة الورق",
               "وزارة الكهرباء والماء"
            ]
        
        speak_output = ", ".join(list_)
        
        
        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )

class certificate_swccIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("certificate_swcc")(handler_input)

    def handle(self, handler_input):
        list_ = [
               "شـــهـادة أعـتـماد المعهد القانوني لإدارة الــبـــيـــئـــة والمياه",
               "رخصـة أعتماد أختبار الـتـنـاضح الـعكـسي من الجمعية الدولية للتدريب والتطوير",
               "رخصة تقديـم خدمات دورات واخـتـبـارات برنامـج الايلتس",
               "شـــهـادة أعـتـماد المنهج البريطاني 2008",
               "شـــهــادة أعــتــمـاد الـــمـــركز الـوطـنـي للتعليم الإلكتروني 2022",
               "رخـــصــة أعــتــمــاد مــن الــمــنــظــمـة الـدولــيــة لــرخصة الذكاء الاصطناعي",
               "شــهـادة أعـتماد الــرابـطة الدولية للتعليم المستمر والـتدريـب 2020",
            ]
        
        speak_output = ", ".join(list_)
        
        
        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class programs_swccIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("programs_swcc")(handler_input)

    def handle(self, handler_input):

        speak_output = ", ".join(names_program)
        
        
        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "أَنَا لَسْتُ مُتَأَكِّدَةً مَاذَا تُرِيدُ"
        reprompt = "أَنَا لَمْ أَتَمَكَّنْ مِنْ ذَلِكَ كَيْفَ أُسَاعِدُكُ"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class generaldateRequestIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("date")(handler_input)
    
    def handle(self, handler_input):
        speak_output = 'اليوم هو, '+datetime.now().strftime("%B %d, %Y")
        
        return (
           handler_input.response_builder.speak(speak_output).ask(speak_output).response
        ) 


class time_arabicRequestIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("time")(handler_input)
    
    def handle(self, handler_input):
        
        tz = pytz.timezone('Asia/Riyadh')
        speak_output = 'اَلتَّوْقِيت اَلْآنِ, '+datetime.now(tz).strftime("%I:%M %p")

       
        return (
           handler_input.response_builder.speak(speak_output).ask(speak_output).response
        ) 

class open_twitterRequestIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("open_twitter")(handler_input)

    def handle(self, handler_input):
        speak_output = "تم فتح تويتر"

        if get_supported_interfaces(handler_input).alexa_presentation_apl is not None:

            return (
                handler_input.response_builder.speak(speak_output)
                .ask("A reprompt to keep the session open")
                .add_directive(
                    RenderDocumentDirective(
                        token="pagerToken",
                        document=_load_apl_document("open.json"),
                        datasources={},
                    )
                )
                .response
            )

        else:
            speak_output = "يوجد خطأ للوصول للموقع"
            return (
                handler_input.response_builder.speak(speak_output)
                .ask("Please buy an Alexa device with a screen")
                .response
            )


class open_websiteRequestIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("open_website")(handler_input)

    def handle(self, handler_input):
        speak_output = "تم فتح الموقع"

        if get_supported_interfaces(handler_input).alexa_presentation_apl is not None:

            return (
                handler_input.response_builder.speak(speak_output)
                .ask("A reprompt to keep the session open")
                .add_directive(
                    RenderDocumentDirective(
                        token="pagerToken",
                        document=_load_apl_document("open2.json"),
                        datasources={},
                    )
                )
                .response
            )

        else:
            speak_output = "يوجد خطأ للوصول للموقع"
            return (
                handler_input.response_builder.speak(speak_output)
                .ask("Please buy an Alexa device with a screen")
                .response
            )

class who_swccIntentHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("who_swcc")(handler_input)
    
    def handle(self, handler_input):
        
        speak_output = "انا s w c c مساعدك الذكي"
        return (
           handler_input.response_builder.speak(speak_output).ask(speak_output).response
        ) 

class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "لا استطيع فهم سؤالك"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())

sb.add_request_handler(lamha_swccIntentHandler())
sb.add_request_handler(dor_swccIntentHandler())

sb.add_request_handler(mnhag_swccIntentHandler())

sb.add_request_handler(rowya_swccIntentHandler())
sb.add_request_handler(rsalat_swccIntentHandler())

sb.add_request_handler(targets_swccIntentHandler())

sb.add_request_handler(values_swccIntentHandler())

sb.add_request_handler(stations_swccIntentHandler())

sb.add_request_handler(marafaq_swccIntentHandler())

sb.add_request_handler(masarat_swccIntentHandler())

sb.add_request_handler(masoula_swccIntentHandler())

sb.add_request_handler(outputs_swccIntentHandler())

sb.add_request_handler(programs_swccIntentHandler())

sb.add_request_handler(generaldateRequestIntentHandler())

sb.add_request_handler(time_arabicRequestIntentHandler())

sb.add_request_handler(open_twitterRequestIntentHandler())

sb.add_request_handler(open_websiteRequestIntentHandler())

sb.add_request_handler(who_swccIntentHandler())

sb.add_request_handler(partener_swccIntentHandler())

sb.add_request_handler(certificate_swccIntentHandler())

sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
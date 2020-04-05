# dic_academic_api
Access to dic.academic.ru api

installation: pip install -e git://github.com/drforse/dic_academic_api.git#egg=dic_academic_api

uninstallation: pip uninstall dic_academic_api

Example with instructions:

    from dic_academic_api import Dic

    # dic name can be found in dic link, ex.: dic.academic.ru/contents.nsf/enc2p/ --> enc2p
    #                                         lopatin.academic.ru/ --> lopatin
    results = Dic(dic='enc2p').get_word_results(q='слово', limit=20)
    
    # results is a list of WordResult-objects
    # You can see what is in WordResult object like this:
    print(results[0])
    or:
    print(results[0].to_python())
    # and get json as:
    json_result_word = results[0].to_json()

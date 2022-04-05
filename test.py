import collections

bool_text = """a    about   above   across   after   again   against   all   almost
Alone   along   alredy   also   although   always   among   an   and
Another   any   anybody   anyone   anything   anywhere   are   area   areas
Around   as   ask   asked   asking   asks   at   away   be
Because   became   become   becomes   been   before   began   behind   being
Both   but   by   c   came   can   cannot   case   cases
Certain   certainly   clear   clearly   come   could   d   did   differ
Different      differently   do   does   done   down   downed   downing
Downs      during   e   each   early   either   end   ended
Ending   ends   enough   even   evenly   ever   every   everybody   everyone
everything   everywhere   f   face   faces   fact   facts   far   
Felt   few   find   finds   first   for   four   from   full
Fully   further   furthered   furthering   furthers   g   gave   general   generally
Get   gets   give   given   gives   go   going   good   goods
Got   great   greater   greatest   group   grouped   grouping   groups   h
Had   has   have   having   he   her   herself   here   high
Higher   highest   him   himself   his   how   however   I   if
important   in   interest   interested   interesting   interests   into   is"
It   its   itself   j   just   k   keep"""

def list_return(text:str) -> list:
    text = text.lower()
    return text.split()

def check_bool(text:list, bool_text:list) -> dict:
    dic = collections.defaultdict(int)
    
    for index in range(len(text)):
        if test[index] not in bool_text:
            dic[test[index]] += 1

    return dic

if __name__ == "__main__":
    bool_text = list_return(bool_text)
    
    test = "I am a teacher, and I am a women"
    test = list_return(test)
    
    result = check_bool(test,bool_text)
    
    for str in result.keys():
        print(str)

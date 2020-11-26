class CSVHandler():

    def exportClub(clubs):
        content = 'Name|Province|Address\n'
        for club in clubs:
            content += club.name + '|' 
            content += club.province + '|' 
            content += club.address + '\n' 
            # content += club.contact + '\n'
        return content

    def importClub(file):
        return "123"

    def exportClubMember(members):
        content = 'Name|Rank|Hometown|BirthYear\n'
        for member in members:
            content += member.name + '|' 
            content += str(member.rank) + '|' 
            content += str(member.hometown.strip()) + '|'
            content += str(member.birthYear) + '\n' 
            # content += club.contact + '\n'
        return content

    def importClubMember(file):
        return "123"
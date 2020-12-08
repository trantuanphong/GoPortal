class CSVHandler():

    def exportClub(clubs):
        content = 'Name|Province|Address\n'
        for club in clubs:
            row = ''
            row += club.name + '|' 
            row += club.province + '|' 
            row += club.address + '|' 
            row += club.contact.strip() + '\n'
            content += CSVHandler.cleanString(row)
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

    def cleanString(content):
        content = content.strip().replace('\n',' ')
        content += '\n'
        return content
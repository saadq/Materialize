# This is a comment

class Person

  attr_accessor :name

  def initialize(attributes = {})
    @name = attributes[:name]
  end

  def self.greet
    "hello"
  end

end

person = Person.new(:name => "Saad")
print Person::greet, " ", person1.name, "\n"
puts "another #{Person::greet} #{person1.name}"
namespace :db do
  desc "Fill database with sample data"
  task populate: :environment do
    5.times do |n|
      sex = "Girl"
      password = "password"
      age = 20
      school = "seu"
      User.create!(
				   sex: sex,
				   password: password,
				   school: school,
				   age: age,)
    end

    5.times do |n|
      ufile = Ufile.new
      ufile.save
    end

    users = User.all
    5.times do
      price = 0.5
      state = "Paid"
      users.each { |user| user.uorders.create!(price: price,
      											state: state)}
    end

    uorders = Uorder.all
    5.times do
      ufile_id = rand(1..5)
      perpage = 1
      uorders.each{ |uorder| uorder.uprints.create!(ufile_id: ufile_id,
                                                  perpage: perpage)}
    end

  end
end
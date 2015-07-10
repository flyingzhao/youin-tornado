class AddManythings < ActiveRecord::Migration
  def change

    add_column :users, :phone, :string
    add_column :users, :sex, :string
    add_column :users, :age, :integer
    add_column :users, :remember_token, :string
    add_index :users, :remember_token
    add_column :users, :school, :string
    add_column :users, :major, :string
    add_column :users, :password, :string
end
end

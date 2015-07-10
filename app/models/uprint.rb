class Uprint < ActiveRecord::Base
	belongs_to :uorder
	default_scope -> { order('created_at DESC') }  	
  	validates :uorder_id, presence: true
  	
	belongs_to :ufile
	default_scope -> { order('created_at DESC') }  	
  	validates :ufile_id, presence: true
end
